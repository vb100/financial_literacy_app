import { useEffect, useState } from 'react';
import { fetchLatestFeed } from '../api/feed';
import { FeedResponse } from '../types/feed';

export function useFeed() {
  const [feed, setFeed] = useState<FeedResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchLatestFeed()
      .then(setFeed)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  return { feed, loading, error };
}
