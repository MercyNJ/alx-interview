#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function fetchMovieCharacters (characters) {
  let processedCharacters = 0;

  function processCharacter (characterUrl) {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.log(error);
      } else {
        console.log(JSON.parse(body).name);
      }

      processedCharacters++;

      if (processedCharacters === characters.length) {
        // All characters processed

      }
    });
  }

  characters.forEach(processCharacter);
}

request(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    fetchMovieCharacters(characters);
  }
});
