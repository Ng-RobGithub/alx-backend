#!/usr/bin/env node
import express from 'express';
import { promisify } from 'util';
import { createClient } from 'redis';

// Define product list
const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5
  },
];

// Create and connect Redis client
const client = createClient();

// Handle Redis connection errors
client.on('error', (err) => {
  console.error('Redis Client Error:', err);
});

const connectRedis = async () => {
  try {
    console.log('Connecting to Redis...');
    await client.connect();
    console.log('Connected to Redis');
  } catch (err) {
    console.error('Error connecting to Redis:', err);
  }
};

// Promisify Redis commands
const setAsync = promisify(client.SET).bind(client);
const getAsync = promisify(client.GET).bind(client);

const getItemById = (id) => {
  const item = listProducts.find(obj => obj.itemId === id);
  if (item) {
    return { ...item }; // Use spread operator to return a copy
  }
};

// Initialize Express app
const app = express();
const PORT = 1245;

// Reserve stock function
const reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock);
};

// Get current reserved stock function
const getCurrentReservedStockById = async (itemId) => {
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock, 10) : 0;
};

// List all products route
app.get('/list_products', (_, res) => {
  res.json(listProducts);
});

// Get product by ID route
app.get('/list_products/:itemId(\\d+)', async (req, res) => {
  const itemId = Number.parseInt(req.params.itemId, 10);
  const productItem = getItemById(itemId);

  if (!productItem) {
    return res.status(404).json({ status: 'Product not found' });
  }

  try {
    const reservedStock = await getCurrentReservedStockById(itemId);
    productItem.currentQuantity = productItem.initialAvailableQuantity - reservedStock;
    res.json(productItem);
  } catch (error) {
    res.status(500).json({ status: 'Error retrieving stock' });
  }
});

// Reserve product route
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number.parseInt(req.params.itemId, 10);
  const productItem = getItemById(itemId);

  if (!productItem) {
    return res.status(404).json({ status: 'Product not found' });
  }

  try {
    const reservedStock = await getCurrentReservedStockById(itemId);
    if (reservedStock >= productItem.initialAvailableQuantity) {
      return res.json({ status: 'Not enough stock available', itemId });
    }
    
    await reserveStockById(itemId, reservedStock + 1);
    res.json({ status: 'Reservation confirmed', itemId });
  } catch (error) {
    res.status(500).json({ status: 'Error reserving stock' });
  }
});

// Reset stock function
const resetProductsStock = async () => {
  console.log('Resetting stock...');
  await Promise.all(
    listProducts.map(
      item => setAsync(`item.${item.itemId}`, 0)
    )
  );
  console.log('Stock reset complete');
};

// Start server
app.listen(PORT, async () => {
  console.log('Starting server...');
  try {
    await connectRedis(); // Ensure Redis connection is established
    await resetProductsStock();
    console.log(`API available on localhost port ${PORT}`);
  } catch (error) {
    console.error('Error initializing stock:', error);
  }
});

export default app;
