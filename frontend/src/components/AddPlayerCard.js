import React from 'react';

import PropTypes from 'prop-types';

import Player from './Player';
import AddPlayerForm from './AddPlayerForm';

const MAX_CLUE_PLAYERS = 6;

export default function AddPlayerCard({ players }) {
  return (
    <div className="add-player-card">
      <h2>Add Players</h2>
      {
        // Map on a list of integers from 0 to MAX_CLUE_PLAYERS
        [...Array(MAX_CLUE_PLAYERS).keys()].map( i => {
          if (i < players.length) {
            return <Player key={i} player={players[i]} />;
          } else {
            return <div key={i} className="list-box-empty"></div>;
          }
        })
      }
      <AddPlayerForm />
    </div>
  );
}
AddPlayerCard.propTypes = {
  players: PropTypes.arrayOf(Player.propTypes.player)
}
