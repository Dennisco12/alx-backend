import { print, createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const updateHash = (hashName, fieldName, fieldValue) => {
  client.hset('HolbertonSchools', 'Portland', 50, print)
  client.hset('HolbertonSchools', 'Seattle', 80, print)
  client.hset('HolbertonSchools', 'New York', 20, print)
  client.hset('HolbertonSchools', 'Bogota', 20, print)
  client.hset('HolbertonSchools', 'Cali', 40, print)
  client.hset('HolbertonSchools', 'Paris', 2, print)
};

client.on('connect', () => {
  console.log('Redis client connected to the server');
  updateHash();
  client.hgetall('HolbertonSchools', (_err, response) => {
    console.log(response);
  });
});
