#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

async function main () {
  try {
    request(url, async (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      if (response.statusCode === 200) {
        const film = JSON.parse(body);
        const characters = film.characters;
        for (const characterUrl of characters) {
          try {
            const characterData = await new Promise((resolve, reject) => {
              request(characterUrl, (error, response, characterBody) => {
                if (error) {
                  reject(error);
                } else {
                  const character = JSON.parse(characterBody);
                  resolve(character.name);
                }
              });
            });
            console.log(characterData);
          } catch (characterError) {
            console.error('Character Error:', characterError);
          }
        }
      } else {
        console.log('Error code: ' + response.statusCode);
      }
    });
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
