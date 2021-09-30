import React from 'react';

export default function AddPlayerForm() {
  return (
    <form className="add-player-form">
      <div className="add-player-form-control" id="player-name-form-control">
        <input type="text" name="name" id="player-name-field"/>
        <label for="player-name-field">Player name</label>
      </div>
      <div className="add-player-form-control" id="hand-size-form-control">
        <input type="text" name="hand-size" id="hand-size-field"/>
        <label for="hand-size-field">Hand size</label>
      </div>
      <div className="add-player-form-control" id="add-player-submit-control">
        <input
          type="submit"
          value="Add player"
          id="add-player-button"
        />
      </div>
    </form>
  );
}
