#!/usr/bin/node

const request = require('request');

const swapiBaseUrl = 'https://swapi-api.alx-tools.com/api/';

function getCharactersForMovie (movieId) {
  const movieUrl = `${swapiBaseUrl}films/${movieId}/`;

  request(movieUrl, { json: true }, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error('Error:', error || response.statusCode);
      return;
    }
    const characterUrls = body.characters;

    characterUrls.forEach((characterUrl) => {
      request(characterUrl, { json: true }, (
        charError, charResponse, charBody) => {
        if (!charError && charResponse.statusCode === 200) {
          console.log(charBody.name);
        } else {
          console.error('Error:', charError || charResponse.statusCode);
        }
      });
    });
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('movie ID required');
} else {
  getCharactersForMovie(movieId);
}
