import './App.css';
import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState(null);
  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:8000/dummy-result');  
      const jsonData = await response.json();
      setData(jsonData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  useEffect(() => {
    fetchData();
  }, [])

  return (
    <div className="App">
      {data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : (
        <p>Loading data...</p>
      )}
    </div>
  );
}

export default App;
