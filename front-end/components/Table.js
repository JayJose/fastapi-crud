import { Table } from "react-bootstrap";

export default function MyTable() {
  //get data
  const data = [
    {
      id: 1,
      username: "johnny69",
      created_at: "2022-12-03T18:19:08.568813",
    },
    {
      id: 2,
      username: "jayjose",
      created_at: "2022-12-04T16:46:42.312103",
    },
  ];

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
        {data.map((e) => {
          return (
            <tr>
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
