import "bootstrap/dist/css/bootstrap.min.css";
import Head from "next/head";
import styles from "../styles/Home.module.css";

import Form from "../components/Form";
import Table from "../components/Table";
import { Stack } from "react-bootstrap";

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Next & FastAPI</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Stack directional="vertical" gap={4} className="col-md-10 mx-auto my-5">
        <h4>Create a new user</h4>
        <Form />
        <h4>Displaying current users</h4>
        <Table />
      </Stack>
    </div>
  );
}
