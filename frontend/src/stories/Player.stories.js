import React from 'react';

import Player from '../components/Player';

export default {
  component: Player,
  title: 'Player',
};

const Template = (args) => <Player {...args} />;

export const Default = Template.bind({})
Default.args = {
  player: {
    id: 1,
    name: 'Bob',
    hand_size: 3,
  },
};
