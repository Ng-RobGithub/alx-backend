#!/usr/bin/yarn dev
import { createClient } from 'redis';

// Create a Redis client
const client = createClient();

// Log when the client connects successfully
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Log when the client encounters an error
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Connect to Redis
client.connect();
