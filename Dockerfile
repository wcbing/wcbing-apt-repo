FROM debian:12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    apt-utils \
    python3-apt \
    python3-requests \
    curl \
    jq \
    gpg \
    gpg-agent && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /mnt

CMD ["/bin/bash"]