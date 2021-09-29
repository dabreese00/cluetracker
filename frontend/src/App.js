import React, { useState, useEffect } from 'react';
import Api from './lib/api';

const username = process.env.REACT_APP_API_USERNAME;
const password = process.env.REACT_APP_API_PASSWORD;
const api = new Api();
const emptyGameList = {
  "count": 0,
  "next": null,
  "previous": null,
  "results": []
}

function Login () {
  return (
    <button className="login-button">
      Login
    </button>
  );
}

//function PlayerList() {
//  const [players, setPlayers] = useState({});
//
//  return (
//    <div>
//      {players.results.map(item => (
//        <div key={item.id}>
//          <h2>Player {item.name}</h2>
//          <span><p>{item.hand_size}</p></span>
//          <span><p>{item.url}</p></span>
//        </div>
//      ))}
//    </div>
//  );
//}
//
//function AddPlayer() {
//  return (
//    <form>
//      <label>
//        Name:
//        <input type="text" name="name"/>
//        <input type="text" name="cardcount"/>
//      </label>
//      <input type="submit" value="Add"/>
//    </form>
//  );
//}
//
//function CreateGame() {
//  // state i
//  return (
//    <div>
//      <PlayerList />
//      <AddPlayer />
//      <input type="submit" value="Done entering players"/>
//    </div>
//  );
//}

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
