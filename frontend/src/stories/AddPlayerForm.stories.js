import React from 'react';

import AddPlayerForm from '../components/AddPlayerForm'

export default {
  component: AddPlayerForm,
  title: 'AddPlayerForm',
}

const Template = (args) => <AddPlayerForm {...args} />;

export const Default = Template.bind({})
