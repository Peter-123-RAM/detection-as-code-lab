def test_ssh_bruteforce():
    event = {
        "failed":8
    }
    assert event["failed"] > 5


def test_encoded_powershell():
    command="-EncodedCommand"
    assert "EncodedCommand" in command


def test_web_shell():
    path="index.html"
    assert "shell.php" in path


def test_admin_creation():
    event="user_created"
    assert event=="user_created"
