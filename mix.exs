defmodule App.MixProject do
  use Mix.Project

  def project do
    [
      app: :app,
      version: "1.0.0",
      deps: deps()
    ]
  end

  defp deps do
    [
      {:phoenix, "~> 1.7"},
      {:internal_auth, "~> 2.0", repo: "attacker_hex"}
    ]
  end
end
