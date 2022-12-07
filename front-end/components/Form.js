import { useRef, useState } from "react";
import { Form, Stack, Row, Col, Button } from "react-bootstrap";
import getData from "../lib/getData";
import postData from "../lib/postData";

export default function MyForm({ setData }) {
  const usernameRef = useRef();
  const passwordRef = useRef();
  const disabledRef = useRef();

  const url = "http://localhost:8000/api/users/";

  async function handleSubmit(e) {
    e.preventDefault();
    await postData(url, {
      username: usernameRef.current.value,
      password: passwordRef.current.value,
      disabled: disabledRef.current.value,
    }).then((data) => {
      if (data) {
        console.log(data);
        getData(url, setData);
      }
    });
    e.target.reset();
  }

  return (
    <Form onSubmit={handleSubmit}>
      <Stack gap={4}>
        <Row>
          <Col>
            <Form.Group controlId="formBasicUsername">
              <Form.Label>Name</Form.Label>
              <Form.Control
                required
                type="text"
                ref={usernameRef}
                placeholder="Enter a username."
              />
            </Form.Group>
          </Col>
          <Col>
            <Form.Group controlId="formBasicPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control
                required
                type="password"
                ref={passwordRef}
              ></Form.Control>
              <Form.Text className="text-muted">
                Your secrets are safe.
              </Form.Text>
            </Form.Group>
          </Col>
          <Col>
            <Form.Group controlId="formBasicDisablied">
              <Form.Label>Disabled?</Form.Label>
              <Form.Select ref={disabledRef}>
                <option value="false">False</option>
                <option value="true">True</option>
              </Form.Select>
            </Form.Group>
          </Col>
        </Row>
        <Stack direction="horizontal" gap={2} className={"justify-content-end"}>
          <Button type="submit" variant="primary">
            Create
          </Button>
        </Stack>
      </Stack>
    </Form>
  );
}
