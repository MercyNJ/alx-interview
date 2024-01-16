#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function fetchMovieCharacters (characters, index) {
  if (characters.length === index) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      fetchMovieCharacters(characters, index + 1);
    }
  });
}

request(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;

    fetchMovieCharacters(characters, 0);
  }
});
