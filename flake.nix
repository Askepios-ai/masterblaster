{
  description = "Masterblaser Flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
  };

  outputs = {
    self,
    nixpkgs,
  }: let
    # Helpers for producing system-specific outputs
    supportedSystems = ["x86_64-linux" "aarch64-darwin"];
    forEachSupportedSystem = f:
      nixpkgs.lib.genAttrs supportedSystems (system:
        f {
          pkgs = import nixpkgs {inherit system;};
        });
  in {
    # Development environments
    devShells = forEachSupportedSystem ({pkgs}: {
      default = pkgs.mkShell {
        # Pinned packages available in the environment
        packages = with pkgs; [
          python311
          (with python311Packages; [
            aiohttp
            dateutils
          ])
        ];

        # Environment variables
        env = {
          ACCESS_TOKEN = "";
          ORG_ID = "";
          ORG_NAME = "";
          MB_BASE_URL = "https://app.bedriftsligaen.no/api";
          NUMBER_OF_MEMBERS = "";
          TEAM_NAME = "";
        };

        # A hook run every time you enter the environment
        # Can load variables from `.env` file
        shellHook = ''
          set -a; source .env; set +a
        '';
      };
    });
  };
}
