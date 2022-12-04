import { useRef, useState } from "react";
import { Form, Stack, Row, Col, Button } from "react-bootstrap";

export default function MyForm() {
  const [message, setMessage] = useState();

  const usernameRef = useRef();
  const passwordRef = useRef();

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      let req = await fetch("http://localhost:8000/api/users/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: usernameRef.current.value,
          password: passwordRef.current.value,
        }),
      });
      let res = await req.json();
      if (req.status === 201) {
        console.log(res);
        console.log("User successfully created.");
      }
    } catch (err) {
      console.log(err);
    }
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
