import React from 'react';
import PropTypes from 'prop-types';

export default function Player(
  {
    player: {
      id,
      name,
      hand_size
    }
  }
) {
  return (
    <div className="list-item list-box-default">
      {name + "  |  " + hand_size + " cards in hand"}
    </div>
  );
}
Player.propTypes = {
  player: PropTypes.shape({
    id: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    hand_size: PropTypes.number.isRequired,
  })
}
