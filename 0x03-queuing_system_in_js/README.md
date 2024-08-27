0x03-queuing_system_in_js

# Redis Queuing System in JavaScript

## Project Setup

1. **Install Redis:**
   - Follow the instructions to install Redis on your machine. Ensure it is running on port `6380`.

2. **Install Node.js Dependencies:**
   - Navigate to your project directory and install the Redis client:
     ```sh
     npm install redis --legacy-peer-deps
     ```

3. **Run the Node.js Script:**
   - Create and run a script to interact with Redis:
     ```sh
     node index.js
     ```

## Basic Redis Operations

- **Set a Key-Value Pair:**
  ```js
  client.set('Holberton', 'School', (err, reply) => {
      console.log('Set:', reply);
  });
