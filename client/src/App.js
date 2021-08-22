import React, { useState, useEffect } from "react";

import "./App.css";

function App() {
	const [greetings, setGreetings] = useState([]);

	useEffect(() => {
		fetch("http://localhost:8000/test")
			.then((data) => data.json())
			.then((result) => {
				setGreetings(result.message);
			})
			.catch((e) => console.error(e));
	}, [greetings]);

	return <div className="App">{greetings}</div>;
}

export default App;
