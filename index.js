const { Client, RichPresence } = require("discord.js-selfbot-v13");
const fs = require("fs");
const { tokens } = require("./config.json");

const clients = [];

tokens.forEach(tokenData => {
  const client = new Client();

  client.on("ready", async () => {
    console.log(`${client.user.username} is ready!`);

    const currentDate = new Date();
    const expirationDate = new Date(tokenData.day);

    if (expirationDate < currentDate) {
        console.log(`Expiration date (${tokenData.day}) has passed for ${client.user.username}. Skipping...`);
        return;
    }

    const r = new RichPresence()
        .setApplicationId("817229550684471297")
        .setType(tokenData.type)
        .setState(tokenData.state)
        .setName(tokenData.name)
        .setDetails(tokenData.details)
        .setStartTimestamp(Date.now())

    try {
        r.setAssetsLargeImage(tokenData.largeimage);
        r.setAssetsLargeText(tokenData.largete);
    } catch (error) {
        console.error(`Error setting large image for ${client.user.username}: ${error.message}`);
    }

    try {
        r.setAssetsSmallImage(tokenData.smallimage);
        r.setAssetsSmallText(tokenData.smallte);
    } catch (error) {
        console.error(`Error setting small image for ${client.user.username}: ${error.message}`);
    }

    if (tokenData.button1 && tokenData.button1link) {
        r.addButton(tokenData.button1, tokenData.button1link);
    }
    if (tokenData.button2 && tokenData.button2link) {
        r.addButton(tokenData.button2, tokenData.button2link);
    }

    client.user.setActivity(r);
});

  client.on('error', error => {
      console.error(`Error occurred with token ${tokenData.token}: ${error.message}`);
  });

  client.login(tokenData.token).catch(error => {
      console.error(`Error logging in with token ${tokenData.token}: ${error.message}`);
  });

  clients.push(client);
});

Promise.all(clients.map(client => {
  return new Promise((resolve, reject) => {
      client.once('ready', () => {
          resolve();
      });
      client.once('error', (error) => {
          reject(error);
      });
  });
}))

