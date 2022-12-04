import { useEffect, useState } from "react";
import { Table } from "react-bootstrap";
import getData from "../lib/getData";

export default function MyTable() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    getData("http://localhost:8000/api/users/", setUsers);
  }, []);

  function formatDate(date) {
    let options = { hour: "2-digit", minute: "2-digit" };
    let newDate = new Date(date);
    return newDate.toLocaleDateString("en-US", options);
  }

  return (
    <Table striped bordered hover>
      <thead>
        <tr>
          <th>Id</th>
          <th>Username</th>
          <th>Created on</th>
        </tr>
      </thead>
      <tbody>
        {users.map((e) => {
          return (
            <tr key={e.id}>
              <td>{e.id}</td>
              <td>{e.username}</td>
              <td>{formatDate(e.created_at)}</td>
            </tr>
          );
        })}
      </tbody>
    </Table>
  );
}
