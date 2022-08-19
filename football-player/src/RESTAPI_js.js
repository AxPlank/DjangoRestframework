import React, { useState } from "react";
import axios from "axios";
import "./RESTAPI_css.css"

function App() {
    const [data, setData] = new useState([]);

    axios.get("http://127.0.0.1:8000/").then((response) => {
        setData([...response.data]);
        console.log("SUCCESS");
    })
    .catch(function(error) {
        console.log("FAILED!");
        console.log(error);
    });

    return (
        <div>
            <h1>Gunners</h1>
            <table>
                <thead>
                    <tr>
                        <td>Profile Image</td>
                        <td>Name</td>
                        <td>Position</td>
                        <td>Uniform Number</td>
                    </tr>
                </thead>
                <tbody>
                    {data.map((e, keyy) => (
                        <tr key={ keyy }>
                            <td><img className="image-size" src={ e.profile_img }/></td>
                            <td>{ e.name }</td>
                            <td>{ e.position }</td>
                            <td>{ e.uniform_number }</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default App;