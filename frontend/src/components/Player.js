import React from 'react';

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
    <div className="list-item">
      <input type="text" value={name} readOnly={true} />
    </div>
  );
}
