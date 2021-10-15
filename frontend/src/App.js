import React, { useState, useEffect } from 'react';
import Api from './lib/api';
import AddPlayerCard from './components/AddPlayerCard';

const username = process.env.REACT_APP_API_USERNAME;
const password = process.env.REACT_APP_API_PASSWORD;
const api = new Api();
const emptyGameList = {
  "count": 0,
  "next": null,
  "previous": null,
  "results": []
}
const dummyPlayers = [
    { id: 1, name: 'Player 1', hand_size: 4 },
    { id: 2, name: 'Player 2', hand_size: 3 },
    { id: 3, name: 'Player 3', hand_size: 3 },
];

function Login () {
  return (
    <button className="login-button">
      Login
    </button>
  );
}

function App () {
  const [games, setGames] = useState(emptyGameList);

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
  }, []);

  return (
    <div>
      <div className="login"><Login /></div>
      <h1>ClueTracker</h1>
      <AddPlayerCard players={dummyPlayers}/>
      <h2>Games</h2>
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
