package main

import (
	"fmt"
	// "go/constant"
	"log"
	"myproject/utils"
	"os"

	"github.com/gofiber/fiber/v2"
	// "github.com/gofiber/fiber/v2/utils"
	"github.com/joho/godotenv"
	"strconv"
)
func Load_dotenv() map[string]string {
    if godotenv.Load("../.env") != nil{
        log.Fatal("Unable to load .env file")
    }
    env := make(map[string]string)
    env["SERVER_HOST"] = os.Getenv("SERVER_HOST")
	env["SERVER_PORT"] = os.Getenv("SERVER_PORT_FIBER")
	env["MASTER_EMAIL_ALIAS"] = os.Getenv("MASTER_EMAIL_ALIAS")
	env["MASTER_EMAIL_PASSWORD"] = os.Getenv("MASTER_EMAIL_PASSWORD")
	env["MASTER_EMAIL_ID"] = os.Getenv("MASTER_EMAIL_ID")
	env["MASTER_EMAIL_SERVER"] = os.Getenv("MASTER_EMAIL_SERVER")
	env["MASTER_EMAIL_PORT"] = os.Getenv("MASTER_EMAIL_PORT")

    return env
}

func main() {
    // utils.SayHello()

    app := fiber.New()
    var env=Load_dotenv()
	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString("Tamal Mallick")
	})
	app.Post("/email", func(c *fiber.Ctx) error {

		type EmailRequest struct { // request JSON
			Sender_email    string `json:"sender_email"`
			Sender_name     string `json:"sender_name"`
			Receiver_email  string `json:"receiver_email"`
            Email_subject   string `json:"email_subject"`
			Email_body		string `json:"email_body"`
			Reply_email    *string `json:"reply_email"`
		}

		var req EmailRequest
		var err error
		
		err = c.BodyParser(&req); // parsing the JSON request body
        if err != nil {
			return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
				"error": "Invalid request body",
			})
		}

		smtpPort, err := strconv.Atoi(env["MASTER_EMAIL_PORT"])
		if err != nil {
			return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
				"error": "Invalid SMTP port",
			})
		}
		var replyEmail *string
		if req.Reply_email != nil && *req.Reply_email != ""{
			replyEmail= req.Reply_email
		}
		err = utils.SendEmail(
			env["MASTER_EMAIL_SERVER"], smtpPort, env["MASTER_EMAIL_ID"], env["MASTER_EMAIL_PASSWORD"],
			req.Sender_email, req.Sender_name, req.Receiver_email, req.Email_subject, req.Email_body,replyEmail,
		)

		if err != nil {
			return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{ 
				"success": false,
				"message": "Failed to send email",
				"error":   err.Error(),
			})
		}
		return c.JSON(fiber.Map{
			"success": true,
			"message": "Email sent successfully",
		})
	})

    app.Get("/env", func(c *fiber.Ctx) error {
        return c.JSON(fiber.Map{  // response
            "message": "env loaded suseccfully",
			"env": fiber.Map{
                "SERVER_HOST":          env["SERVER_HOST"],
                "SERVER_PORT":          env["SERVER_PORT"],
                "MASTER_EMAIL_ID":      env["MASTER_EMAIL_ID"],
                "MASTER_EMAIL_PASSWORD": env["MASTER_EMAIL_PASSWORD"],
                "MASTER_EMAIL_ALIAS":   env["MASTER_EMAIL_ALIAS"],
                "MASTER_EMAIL_SERVER":  env["MASTER_EMAIL_SERVER"],
                "MASTER_EMAIL_PORT":    env["MASTER_EMAIL_PORT"],
			},
        })
	})

	// Start server on port 3000
	// log.Fatal(app.Listen(":3000"))
    log.Fatal(app.Listen(fmt.Sprintf("%s:%s", env["SERVER_HOST"], env["SERVER_PORT"])))
}
