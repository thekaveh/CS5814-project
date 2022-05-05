class IterationDataPoint:
    COL_NAME_LOSS = "loss"
    COL_NAME_MB_IDX = "idx_mb"
    COL_NAME_ITER_IDX = "idx_iter"
    COL_NAME_EPOCH_IDX = "idx_epoch"

    COL_NAMES = [
        COL_NAME_EPOCH_IDX
        , COL_NAME_MB_IDX
        , COL_NAME_ITER_IDX
        , COL_NAME_LOSS
    ]

    def __init__(
        self
        , iter_idx
        , epoch_idx
        , mini_batch_idx
        , loss
    ):
        self.data = {}

        self.data[IterationDataPoint.COL_NAME_EPOCH_IDX] = epoch_idx
        self.data[IterationDataPoint.COL_NAME_MB_IDX] = mini_batch_idx
        self.data[IterationDataPoint.COL_NAME_ITER_IDX] = iter_idx
        self.data[IterationDataPoint.COL_NAME_LOSS] = loss

    def __str__(self):
        return "IterationDataPoint:\n\t+ epoch_idx: {epoch_idx}\n\t+ mb_idx: {mini_batch_idx}\n\t+ iter_idx: {iter_idx}\n\t+ loss: {loss}\n" \
            .format(
                epoch_idx=self.data[IterationDataPoint.COL_NAME_EPOCH_IDX]
                , iter_idx=self.data[IterationDataPoint.COL_NAME_ITER_IDX]
                , mini_batch_idx=self.data[IterationDataPoint.COL_NAME_MB_IDX]
                , loss=self.data[IterationDataPoint.COL_NAME_LOSS]
            )