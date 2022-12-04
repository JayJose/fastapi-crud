import { Table } from "react-bootstrap";
import formatDate from "../lib/formatDate";

export default function MyTable({ data }) {
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
        {data.map((e) => {
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
