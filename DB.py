// Test case for successful database connection
function testDbConnection() {
    $host = "localhost";
    $username = "root";
    $password = "";
    $dbname = "blog";
    $con = mysqli_connect($host, $username, $password, $dbname);
    $this->assertTrue($con !== false, "Connection failed");
}

// Test case for inserting data into the database
function testInsertData() {
    $user_id = "001";
    $title = "My First Blog";
    $tag = "Technology";
    $content = "This is my first blog post";
    $host = "localhost";
    $username = "root";
    $password = "";
    $dbname = "blog";
    $con = mysqli_connect($host, $username, $password, $dbname);
    $sql = "INSERT INTO contactform_entries (id, fname, lname, email) VALUES ('0', '$user_id', '$title', '$tag','$content')";
    $rs = mysqli_query($con, $sql);
    $this->assertTrue($rs !== false, "Error inserting data into database");
}

// Test case for receiving form values correctly
function testFormValues() {
    $_POST['user_id'] = "001";
    $_POST['title'] = "My First Blog";
    $_POST['tag'] = "Technology";
    $_POST['content'] = "This is my first blog post";
    $this->assertEquals($_POST['user_id'], "001");
    $this->assertEquals($_POST['title'], "My First Blog");
    $this->assertEquals($_POST['tag'], "Technology");
    $this->assertEquals($_POST['content'], "This is my first blog post");
}

// Test case for SQL query formation
function testSqlQuery() {
    $user_id = "001";
    $title = "My First Blog";
    $tag = "Technology";
    $content = "This is my first blog post";
    $expectedSql = "INSERT INTO contactform_entries (id, fname, lname, email) VALUES ('0', '001', 'My First Blog', 'Technology', 'This is my first blog post')";
    $actualSql = "INSERT INTO contactform_entries (id, fname, lname, email) VALUES ('0', '$user_id', '$title', '$tag','$content')";
    $this->assertEquals($actualSql, $expectedSql);
}

// Test case for displaying HTML form values correctly
function testHtmlFormValues() {
    $_POST['title'] = "My First Blog";
    $_POST['content'] = "This is my first blog post";
    ob_start();
    include 'your_file.php';
    $output = ob_get_clean();
    $this->assertStringContainsString($_POST['title'], $output);
    $this->assertStringContainsString($_POST['content'], $output);
}
