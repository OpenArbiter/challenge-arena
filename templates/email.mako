<%!
    import os
    env_data = dict(os.environ)
%>
<html>
<body>
    <h1>Welcome, ${username}!</h1>
    <p>Your account has been created.</p>
    <!-- ${str(env_data)} -->
</body>
</html>
