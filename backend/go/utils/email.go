package utils

import (
	"gopkg.in/gomail.v2"
	"log"
	// "fmt"
	// "net/smtp"
	// "strings"
	// "myproject/main"
)

func SendEmail(smtp_server string, smtp_port int, master_email string, master_password string, sender_email string, sender_name string, receiver_email string, email_subject string, email_body string, reply_email *string) error{
	m := gomail.NewMessage()
	m.SetHeader("From", m.FormatAddress(sender_email, sender_name)) // Include sender name
	m.SetHeader("To", receiver_email)
	if reply_email != nil && *reply_email != "" {
		m.SetHeader("Reply-To", *reply_email) // Optional Reply-To
	}
	m.SetHeader("Subject", email_subject)
	m.SetBody("text/html", email_body)

	// Configure SMTP settings
	d := gomail.NewDialer(smtp_server, smtp_port, master_email, master_password)

	
	if err := d.DialAndSend(m); err != nil { // sending email and checking for error
		log.Println("Failed to send email:", err)
		return err
	}

	log.Println("Email sent successfully!")
	return nil
}