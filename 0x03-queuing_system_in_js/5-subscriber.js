import { createClient, print } from 'redis';

const redisClient = createClient();

redisClient.on('connect', function() {
  console.log('Redis client connected to the server');
});

redisClient.on('error', function(error) {
  console.log(`Redis client not connected to the server: ${error}`);
});