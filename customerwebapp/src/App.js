import './App.css';
import React, { useEffect, useState } from "react";

//import axios from 'axios';

export default function App(){


  const [itemsFromApi, setItemsFromApi] = useState([]);
  const getItemsFromApi = () => {
    fetch('http://0.0.0.0:5000/customers', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        "Accept":"application/json"
      },
    })
    .then(response => response.json())
    .then(data => setItemsFromApi(data))
    .catch(err => console.log(err))
  }

  useEffect(() => {
    getItemsFromApi()
  }, []);


  return (
    <div className="App">
    <h1>Customer Information Access</h1>
      <table className="App-table">
        <thead>
          <tr>
            <th>Customer ID</th>
            <th>Name</th>
          </tr>
        </thead>
        <tbody>
          {itemsFromApi.length > 0 && itemsFromApi && itemsFromApi.map(item => {
            return (
              <tr>
                <th scope="row">{item.cust_id}</th>
                <td>{item.name}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>

      <div>
      {itemsFromApi.length > 0 && itemsFromApi && itemsFromApi.map(item => {
        return (
            <div><h2>{item.name}</h2>
            Gender: {item.gender}<br></br>
            Email: {item.email}<br></br>
            Phone: {item.phone}<br></br>
            Email: {item.email}<br></br>
            Orders: {item.orders.map(order => `${order.order} , `)}</div>

        );
      })}
      </div>

    </div>
  )
}
