import { useRef, useState } from "react";
import { Form, Stack, Row, Col, Button } from "react-bootstrap";
import postData from "../lib/postData";

export default function MyForm() {
  const [message, setMessage] = useState();

  const usernameRef = useRef();
  const passwordRef = useRef();

  async function handleSubmit(e) {
    e.preventDefault();
    await postData("http://localhost:8000/api/users/", {
      username: usernameRef.current.value,
      password: passwordRef.current.value,
    }).then((data) => {
      if (data) {
        console.log(data);
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
              ></Form.Control>
            </Form.Group>
          </Col>
          <Col>
            <Form.Group controlId="formBasicPassword]">
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
        </Row>
        <Stack direction="horizontal" gap={2} className={"justify-content-end"}>
          <Button type="submit" variant="primary">
            Submit
          </Button>
          <Button type="button" variant="outline-secondary">
            Cancel
          </Button>
        </Stack>
      </Stack>
    </Form>
  );
}
