import "bootstrap/dist/css/bootstrap.min.css";
import Head from "next/head";
import styles from "../styles/Home.module.css";

import Form from "../components/Form";

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Next & FastAPI</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Form />
    </div>
  );
}