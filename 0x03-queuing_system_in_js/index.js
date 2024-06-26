const redis = require('redis');

// Create a Redis client
const client = redis.createClient();

// Connect to Redis server
client.on('connect', () => {
  console.log('Connected to Redis');
});

// Handle errors
client.on('error', (err) => {
  console.log('Redis error: ' + err);
});

// Function to handle Redis operations using promises
async function performRedisOperations() {
  try {
    // Set a key-value pair
    await client.set('key', 'value');
    console.log('SET: OK');

    // Get the value of a key
    const value = await client.get('key');
    console.log('GET:', value);

  } catch (err) {
    console.error('Error:', err);
  } finally {
    // Close the connection
    client.quit();
  }
}

// Call the function to perform Redis operations
performRedisOperations();
