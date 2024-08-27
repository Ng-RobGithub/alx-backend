import { createClient, print } from 'redis';

// Create a new Redis client
const client = createClient();

// Handle connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Confirm connection to the Redis server
client.on('connect', () => {
  console.log('Redis client connected to the server');

  // Perform operations after successful connection
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
});

// Function to set a new school in Redis
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};

// Function to get and display a school value from Redis
const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error retrieving value: ${err}`);
      return;
    }
    console.log(reply);
  });
};

// Ensure the client closes properly when the script ends
process.on('SIGINT', () => {
  client.quit(() => {
    console.log('Redis client closed gracefully');
    process.exit(0);
  });
});

process.on('SIGTERM', () => {
  client.quit(() => {
    console.log('Redis client closed gracefully');
    process.exit(0);
  });
});
