import { useEffect, useState } from "react";

import Head from "next/head";
import "bootstrap/dist/css/bootstrap.min.css";
import styles from "../styles/Home.module.css";

import Form from "../components/Form";
import Table from "../components/Table";
import { Stack } from "react-bootstrap";

import getData from "../lib/getData";

export default function Home() {
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
    <div className={styles.container}>
      <Head>
        <title>Next & FastAPI</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Stack directional="vertical" gap={4} className="col-md-10 mx-auto my-5">
        <h4>Create a new user</h4>
        <Form
          onSuccess={getData("http://localhost:8000/api/users/", setUsers)}
        />
        <h4>Displaying current users</h4>
        <Table data={users} />
      </Stack>
    </div>
  );
}
