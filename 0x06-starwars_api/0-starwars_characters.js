#!/usr/bin/node

const request = require('request');

const swapiBaseUrl = 'https://swapi-api.alx-tools.com/api/';

function fetchMovie(movieId, callback) {
  const movieUrl = `${swapiBaseUrl}films/${movieId}/`;

  request(movieUrl, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error('Error fetching movie information:', error || response.statusCode);
      return;
    }

    const parsedBody = JSON.parse(body);
    const characterUrls = parsedBody.characters;
    callback(characterUrls);
  });
}

function fetchCharacter(characterUrl) {
  request(characterUrl, (charError, charResponse, charBody) => {
    const parsedCharBody = JSON.parse(charBody);

    if (!charError && charResponse.statusCode === 200) {
      console.log(parsedCharBody.name);
    } else {
      console.error('Error fetching character information:', charError || charResponse.statusCode);
    }
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as a command line argument.');
} else {
  fetchMovie(movieId, (characterUrls) => {
    characterUrls.forEach((characterUrl) => {
      fetchCharacter(characterUrl);
    });
  });
}
