import { useState } from 'react'
import { MantineProvider, Text } from '@mantine/core'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <MantineProvider withGlobalStyles withNormalizeCSS>
      <Text>Welcome to Mantine!</Text>
    </MantineProvider>
  );
}

export default App
