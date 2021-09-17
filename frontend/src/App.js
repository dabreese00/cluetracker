import React, { useState, useEffect } from 'react';
import Api from './api';

const username = 'admin';
const password = 'admin';

function Login () {
  return (
    <button className="login-button">
      Login
    </button>
  );
}

function App () {
  const [api] = useState(new Api())
  const [games, setGames] = useState(
    {
      "count": 0,
      "next": null,
      "previous": null,
      "results": []
    }
  )

  useEffect(() => {
    const fetchGames = async () => {
      const token = await api.getToken(username, password);
      const games = await api.listGames(token);
      return await games;
    };
    fetchGames().then((games) => {
      setGames(games)
    }).catch(e => {
      console.log('Getting games failed!')
    });
  });

  return (
    <div>
      <div className="login"><Login /></div>
      <h1>ClueTracker</h1>
      {games.results.map(item => (
        <div key={item.id}>
          <h2>Game {item.id}</h2>
          <span><p>{item.url}</p></span>
          <span><p>{item.created_timestamp}</p></span>
        </div>
      ))}
    </div>
  );
}

export default App;
