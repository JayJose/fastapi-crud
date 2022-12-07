import { Button, Table } from "react-bootstrap";
import formatDate from "../lib/formatDate";
import deleteData from "../lib/deleteData";
import getData from "../lib/getData";

export default function MyTable({ data, setData }) {
  const url = "http://localhost:8000/api/users/";

  async function onDelete(id) {
    await deleteData(url, id).then((data) => {
      if (data === "Delete successful.") {
        getData(url, setData);
      }
    });
  }

  return (
    <Table striped bordered hover>
      <thead>
        <tr>
          <th>Id</th>
          <th>Username</th>
          <th>Disabled</th>
          <th>Created on</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {data.map((e) => {
          return (
            <tr key={e.id}>
              <td>{e.id}</td>
              <td>{e.username}</td>
              <td>{String(e.disabled)}</td>
              <td>{formatDate(e.created_at)}</td>
              <td>
                <Button
                  type="button"
                  variant="danger"
                  size="sm"
                  className="button--danger"
                  onClick={() => onDelete(e.id)}
                >
                  Delete
                </Button>
              </td>
            </tr>
          );
        })}
      </tbody>
    </Table>
  );
}
