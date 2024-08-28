#!/usr/bin/env node
import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const updateHash = (hashName, fieldName, fieldValue, callback) => {
  client.HSET(hashName, fieldName, fieldValue, (err, reply) => {
    if (err) {
      console.error('Error setting hash value:', err);
    } else {
      print(reply);
      if (callback) callback(); // Call the callback function once the update is done
    }
  });
};

const printHash = (hashName) => {
  client.HGETALL(hashName, (_err, reply) => {
    if (_err) {
      console.error('Error retrieving hash:', _err);
    } else {
      console.log(reply);
    }
    client.quit(); // Ensure the client quits after the operations
  });
};

function main() {
  const hashObj = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  let operationsLeft = Object.entries(hashObj).length;

  const onOperationComplete = () => {
    operationsLeft--;
    if (operationsLeft === 0) {
      printHash('HolbertonSchools');
    }
  };

  for (const [field, value] of Object.entries(hashObj)) {
    updateHash('HolbertonSchools', field, value, onOperationComplete);
  }
}

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});
