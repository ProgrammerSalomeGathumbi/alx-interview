#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  if (response.statusCode === 200) {
    const film = JSON.parse(body);
    const characters = film.characters;
    function getCharacterData (characterUrl) {
      request(characterUrl, (error, response, characterBody) => {
        if (error) {
          console.log(error);
          return;
        }
        const characterData = JSON.parse(characterBody);
        console.log(characterData.name);
      });
    }

    for (const characterUrl of characters) {
      getCharacterData(characterUrl);
    }
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
