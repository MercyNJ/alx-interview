#!/usr/bin/node

const request = require('request');

function fetchMovieCharacters(movieId) {
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request(movieUrl, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error('Error fetching movie information:', error || response.statusCode);
      return;
    }

    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    characterUrls.forEach((characterUrl) => {
      fetchCharacterName(characterUrl);
    });
  });
}

function fetchCharacterName(characterUrl) {
  request(characterUrl, (charError, charResponse, charBody) => {
    if (!charError && charResponse.statusCode === 200) {
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    } else {
      console.error('Error fetching character information:', charError || charResponse.statusCode);
    }
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as a command line argument.');
} else {
  fetchMovieCharacters(movieId);
}
