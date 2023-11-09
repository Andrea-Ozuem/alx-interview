#!/usr/bin/node

const util = require('util');
const request = util.promisify(require('request'));

const id = process.argv[2];

async function getCharacters (filmId) {
  const filmApi = 'https://swapi-api.alx-tools.com/api/films/' + filmId;
  let res = await request(filmApi);
  if (res.statusCode !== 200) return;
  res = JSON.parse(res.body);
  const characters = res.characters;

  for (let i = 0; i < characters.length; i++) {
    const charApi = characters[i];
    let charRes = await request(charApi);
    if (charRes.statusCode !== 200) return;
    charRes = JSON.parse(charRes.body);
    console.log(charRes.name);
  }
}

getCharacters(id);
