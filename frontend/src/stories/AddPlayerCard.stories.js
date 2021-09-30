import React from 'react';

import AddPlayerCard from '../components/AddPlayerCard';

import * as PlayerStories from './Player.stories';

export default {
  component: AddPlayerCard,
  title: 'AddPlayerCard',
}

const Template = (args) => <AddPlayerCard {...args} />;

export const Default = Template.bind({});
Default.args = {
  players: [
    { ...PlayerStories.Default.args.player, id: 1, name: 'Player 1', hand_size: 4 },
    { ...PlayerStories.Default.args.player, id: 2, name: 'Player 2', hand_size: 3 },
    { ...PlayerStories.Default.args.player, id: 3, name: 'Player 3', hand_size: 3 },
  ],
};
