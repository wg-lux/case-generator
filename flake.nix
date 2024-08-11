{
  description = "Application packaged using poetry2nix";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
    cachix = {
      url = "github:cachix/cachix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, flake-utils, cachix, ... }: #poetry2nix
    let
        system = "x86_64-linux";
        pkgs = import nixpkgs {
          inherit system;
          config.allowUnfree = true;
        };
        venvDir = ".venv";

    in
        {
          # Call with nix develop
          devShell."${system}" = pkgs.mkShell {
            buildInputs = with pkgs; [ 
              poetry
              opencv
              tesseract

              python311
              python311Packages.pandas
              python311Packages.venvShellHook
              python311Packages.numpy
            ];

            # Define Environment Variables
            DJANGO_SETTINGS_MODULE="agl_case_generator.settings";

            # add venvdir binaries to PATH
            venvDir = venvDir;
            # postShellHook = ''
            # export PATH=$PWD/${venvDir}/bin:$PATH
            # '';
          };

      };
}
