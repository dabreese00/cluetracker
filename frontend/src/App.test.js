import { render, screen } from '@testing-library/react';
import App from './App';

test('renders title', () => {
  render(<App />);
  const titleElement = screen.getByText(/ClueTracker/i);
  expect(titleElement).toBeInTheDocument();
});

test('renders login/logout', () => {
  render(<App />);
  const loginElement = screen.getByText(/Log/i);
  expect(loginElement).toBeInTheDocument();
});
